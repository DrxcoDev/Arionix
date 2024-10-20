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
            HBRUSH backgroundBrush = CreateSolidBrush(RGB(0, 0, 0)); // Crear un pincel negro
            FillRect(hdc, &ps.rcPaint, backgroundBrush); // Rellenar el área de la ventana
            DeleteObject(backgroundBrush); // Eliminar el pincel después de usarlo

            // Establecer las coordenadas y tamaño del cuadrado
            int x = 100, y = 80, size = 200; // Tamaño del cuadrado

            // Rellenar el cuadrado con negro
            HBRUSH squareBrush = CreateSolidBrush(RGB(0, 0, 0)); // Crear un pincel negro
            RECT squareRect = { x, y, x + size, y + size }; // Crear un RECT para el cuadrado
            FillRect(hdc, &squareRect, squareBrush); // Rellenar el cuadrado
            DeleteObject(squareBrush); // Eliminar el pincel después de usarlo

            // Dibujar el borde verde
            HPEN borderPen = CreatePen(PS_SOLID, 3, RGB(0, 255, 0)); // Crear un lápiz verde
            HGDIOBJ oldPen = SelectObject(hdc, borderPen); // Seleccionar el lápiz verde
            Rectangle(hdc, x, y, x + size, y + size); // Dibujar el borde del cuadrado

            // Restaurar el lápiz original
            SelectObject(hdc, oldPen);
            DeleteObject(borderPen); // Eliminar el lápiz después de usarlo

            // Dibujar el texto "inventory" en verde
            SetBkMode(hdc, RGB(0, 0, 0)); // Hacer el fondo del texto transparente
            SetTextColor(hdc, RGB(0, 255, 0)); // Color del texto (verde)
            TextOut(hdc, x + 50, y + 90, "inventory", 9); // Dibujar el texto

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
