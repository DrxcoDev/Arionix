import scala.sys.process._

object PythonExecutor {
  def main(args: Array[String]): Unit = {
    // Ruta del archivo Python que deseas ejecutar
    val pythonºFilePath = "main.py"

    // Ejecutar el archivo Python usando el comando de sistema
    val exitCode = s"python $pythonFilePath" !

    // Comprobar el código de salida
    if (exitCode == 0) {
      println("El script de Python se ejecutó correctamente.")
    } else {
      println(s"Hubo un error al ejecutar el script de Python. Código de salida: $exitCode")
    }
  }
}
