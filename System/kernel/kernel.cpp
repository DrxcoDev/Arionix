#include <windows.h>
#include <string>

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            // Fondo negro
            HBRUSH backgroundBrush = CreateSolidBrush(RGB(0, 0, 0)); 
            FillRect(hdc, &ps.rcPaint, backgroundBrush); 
            DeleteObject(backgroundBrush); 

            // Fuente "Consolas"
            HFONT hFont = CreateFont(24, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE,
                                     ANSI_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                                     DEFAULT_QUALITY, FIXED_PITCH | FF_MODERN, "Consolas");
            SelectObject(hdc, hFont);

            // Color del texto y fondo transparente
            SetTextColor(hdc, RGB(0, 255, 0)); 
            SetBkMode(hdc, TRANSPARENT);

            // Texto a mostrar con delay entre palabras
            std::string texto = "Boost images NULL 0x0000";
            TextOut(hdc, 10, 10, texto.c_str(), texto.size());

            std::string CPUON = "Power State: 0D \n Memory_::L1 0x1102";
            TextOut(hdc, 10, 40, CPUON.c_str(), texto.size());
        

            // Mostrar cada letra con un delay
            // for (char c : texto) {
            //     TextOut(hdc, x, y, &c, 1); // Dibujar una letra
            //     x += 20; // Mover la posición del texto
            //     Sleep(500); // Retardo de 500ms entre letras
            // }

            DeleteObject(hFont);
            EndPaint(hwnd, &ps);
        }
        return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nShowCmd) {
    const char CLASS_NAME[] = "Sample Window Class";
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0, CLASS_NAME, "Ventana con delay en texto", WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 800, 600,
        NULL, NULL, hInstance, NULL
    );

    if (hwnd == NULL) {
        return 0;
    }

    ShowWindow(hwnd, nShowCmd);

    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
