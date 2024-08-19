using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        List<string> students = new List<string>();

        Console.WriteLine(students.Count);
        students.Add("Anna");
        Console.WriteLine(students.Count);
        students.Add("Laura");
        Console.WriteLine(students.Count);
        students.Add("Jacob");
        Console.WriteLine(students.Count);
        students.Add("Aron");
        Console.WriteLine(students.Count);
    }
}