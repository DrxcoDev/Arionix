#include <windows.h>

// Función de procesamiento de mensajes
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            // Establecer el color de fondo a negro
            HBRUSH brush = CreateSolidBrush(RGB(0, 0, 0)); // Crear un pincel negro
            FillRect(hdc, &ps.rcPaint, brush); // Rellenar el área de la ventana
            DeleteObject(brush); // Eliminar el pincel después de usarlo

            EndPaint(hwnd, &ps);
        }
        return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nShowCmd) {
    // Nombre de la clase de la ventana
    const char CLASS_NAME[] = "Sample Window Class";

    // Registrar la clase de la ventana
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    // Crear la ventana
    HWND hwnd = CreateWindowEx(
        0,                             // Opciones de estilo
        CLASS_NAME,                   // Nombre de la clase
        "Ventana en Negro",           // Texto de la ventana
        WS_OVERLAPPEDWINDOW,          // Estilo de la ventana
        CW_USEDEFAULT, CW_USEDEFAULT, // Posición
        800, 600,                     // Tamaño
        NULL,                         // Ventana padre
        NULL,                         // Menú
        hInstance,                   // Instancia de la aplicación
        NULL                          // Parámetros adicionales
    );

    if (hwnd == NULL) {
        return 0;
    }

    ShowWindow(hwnd, nShowCmd);

    // Bucle de mensajes
    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
