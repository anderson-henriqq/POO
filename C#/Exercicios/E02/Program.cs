// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography.X509Certificates;

class Program
{
    static void Main(string[] args){
        int a = 0;
        while(a==0){
            Viagem x = new Viagem();
            Console.WriteLine("Digite o tempo em minutos:");
            x.SetTempo(double.Parse(Console.ReadLine()));
            //Console.WriteLine(x.GetTempo());
            Console.WriteLine("Digite o tempo a distancia percorrida em Km:");
            x.SetDistancia(double.Parse(Console.ReadLine()));
            //Console.WriteLine(x.GetDist());
            Console.WriteLine( x.Calc_velo());
            Console.WriteLine("Deseja fazer um novo calculo?:");
            Console.WriteLine("0 - Sim     1 - Não");
            a = int.Parse(Console.ReadLine());
        }
    }
}
