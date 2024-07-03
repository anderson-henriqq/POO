// See https://aka.ms/new-console-template for more information
Circulo x = new Circulo();
Console.WriteLine("Digite o raio:");
x.r = double.Parse(Console.ReadLine()); // O readline ler tudo como string, double.Parse foi necessario para converter string em double
Console.WriteLine(x.area());
Console.WriteLine(x.circun());




