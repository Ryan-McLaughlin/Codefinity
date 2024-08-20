using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        WhatAreLists();
        
        ListDeclaration();

        ListMethods();

        Console.WriteLine();
        Console.WriteLine();
    }

    static void ListMethods()
    {
        Console.WriteLine("***********************************************************");
        Console.WriteLine("* List Methods");
        Console.WriteLine("***********************************************************");
        Console.WriteLine();

    }

    static void ListDeclaration()
    {        
        Console.WriteLine("***********************************************************");
        Console.WriteLine("* List Declaration");
        Console.WriteLine("***********************************************************");
        Console.WriteLine();

        List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        foreach (int num in numbers)
            Console.Write(num + " ");

        Console.WriteLine();
        Console.WriteLine();
    }

    static void WhatAreLists()
    {
        Console.WriteLine("***********************************************************");
        Console.WriteLine("* What are Lists");
        Console.WriteLine("***********************************************************");
        Console.WriteLine();

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

        Console.WriteLine();
    }
}