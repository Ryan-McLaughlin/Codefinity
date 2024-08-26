using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {

        //WhatAreLists();
        //ListDeclaration();
        //ListMethods();
        //WhatAreDictionaries();
        //ReadingFilesUsingStreamReader();
        //ReadingFilesUsingFileMethods();
        UsingStreamWriter();


        Console.WriteLine();
        Console.WriteLine();
    }

    /// <summary> Method UsingStreamWriter()
    /// <para></para>
    /// </summary>
    static void UsingStreamWriter()
    {
        var textFile = new StreamWriter("C:/Users/le-ni/OneDrive/Desktop/tempFile_01");
        textFile.WriteLine("This is some new text.");
        textFile.WriteLine("This is the next line.");
        textFile.WriteLine("Another line.");
        textFile.Close();
    }

    /// <summary> Method ReadingFilesUsingFileMethods()
    /// <para>
    /// This method is to demonstrate reading files using methods
    /// </para>
    /// </summary>
    static void ReadingFilesUsingFileMethods()
    {
        // .ReadAllText() handles openeing and closing file internally ie you don't need to call .Close() on the file
        string tempText = File.ReadAllText("C:/Users/le-ni/OneDrive/Desktop/temp.file");
        Console.WriteLine(tempText);

    }

    /// <summary> Method ReadingFilesUsingStreamReader()
    /// <para>
    /// This method is to demonstrate reading files using StreamReader()
    /// </para>
    /// </summary>
    static void ReadingFilesUsingStreamReader()
    {
        Console.WriteLine();
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine("* StreamReader()");
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine();

        // StreamReader fileVarName = new StreamReader(fullPath);
        StreamReader tempFile = new StreamReader("C:/Users/le-ni/OneDrive/Desktop/temp.file");

        // define line
        string line;
        // assign each read line to 'line' until null is returned
        while ((line = tempFile.ReadLine()) != null)
        {
            Console.WriteLine(line);
        }

        // do not forget to close the file
        tempFile.Close();
    }
    static void WhatAreDictionaries()
    {
        Console.WriteLine();
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine("* What are Dictionaries"); // requires - using System.Collections.Generic;
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine();

        // dictionary declarations
        // IDictionary<keyDataType, valueDataType> dictionaryName = new Dictionary<keyDataType, valueDataType>();

        Console.WriteLine("* dictionary.Add");
        var student = new Dictionary<string, string>();

        student.Add("name", "Noah");
        student.Add("country", "Netherlands");
        student.Add("subject", "Computer Science");

        Console.WriteLine(student["name"]);
        Console.WriteLine(student["country"]);
        Console.WriteLine(student["subject"]);

        Console.WriteLine();
        Console.WriteLine("* dictionary.Count(); dictionary.Remove(); dictionary.Clear()");
        var numbers = new Dictionary<int, string>();

        numbers.Add(0, "Zero");
        numbers.Add(1, "One");
        numbers.Add(2, "Two");
        numbers.Add(3, "Three");
        numbers.Add(4, "Four");
        numbers.Add(5, "Five");

        Console.WriteLine(numbers.Count); // Output: 6
        numbers.Remove(3);
        Console.WriteLine(numbers.Count); // Output: 5
        numbers.Clear();
        Console.WriteLine(numbers.Count); // Output: 0

        Console.WriteLine();
        Console.WriteLine();
        // Declaring a new empty dictionary
        var book = new Dictionary<string, string>();

        // Adding data to the dictionary
        book.Add("name", "The Hobbit");
        book.Add("author", "J. R. R. Tolkien");
        book.Add("publication date", "21 September 1937");

        // Outputting data
        Console.WriteLine("Book Name: " + book["name"]);
        Console.WriteLine("Author: " + book["author"]);
        Console.WriteLine("Publication Date: " + book["publication date"]);
    }

    static void ListMethods()
    {
        Console.WriteLine();
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine("* List Methods");
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine("list.remove() - removes the first element of a list");
        Console.WriteLine();

        List<string> fruits = new List<string> { "Apple", "Banana", "Orange", "Banana", "Grape" };
        Console.WriteLine("Before: ");
        foreach (string fruit in fruits)
        {
            Console.Write(fruit + " ");
        }

        // if no matching element if found list.remove() does not do anything
        fruits.Remove("Banana");

        Console.WriteLine("\nAfter: ");
        foreach (string fruit in fruits)
        {
            Console.Write(fruit + " ");
        }


        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine("list.RemoveAt() - removes at a specific index");
        Console.WriteLine();

        //List<string> fruits = new List<string> { "Apple", "Orange", "Banana", "Grape" };
        fruits.Clear();
        fruits = new List<string> { "Apple", "Orange", "Banana", "Grape" };

        Console.Write("Before: ");
        foreach (string fruit in fruits)
        {
            Console.Write(fruit + " ");
        }

        fruits.RemoveAt(1);

        Console.Write("\nAfter: ");
        foreach (string fruit in fruits)
        {
            Console.Write(fruit + " ");
        }


        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine("list.Clear() - removes all elements from list");

        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine("list.Insert() - inserts an element in the list");
        Console.WriteLine();

        List<int> numbers = new List<int> { 2, 4, 6, 10, 12 };

        Console.Write("Before: ");
        foreach (int number in numbers)
            Console.Write(number + " ");

        // insert at element 3 the number 8 (all elements after 3 are shifted right)
        numbers.Insert(3, 8);

        Console.Write("\nAfter: ");
        foreach (int number in numbers)
            Console.Write(number + " ");


        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine("list.Contains() - checks if list contains a specific element - returns bool");
        Console.WriteLine();

        List<char> vowels = new List<char> { 'a', 'e', 'i', 'o', 'u' };
        Console.WriteLine("Contains 'o': " + vowels.Contains('o'));

        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine("list.IndexOf() - retuns the index of first occurrence of an element in list, no occurrence -1 is returned");
        Console.WriteLine();

        //List<char> vowels = new List<char> { 'a', 'e', 'i', 'o', 'u' };
        vowels.Clear();
        vowels = new List<char> { 'a', 'e', 'i', 'o', 'u' };

        foreach (char vowel in vowels)
        {
            Console.Write(vowel + " ");
        }
        Console.WriteLine();
        Console.WriteLine("Index of 'o': " + vowels.IndexOf('o'));

        vowels.Remove('o');
        foreach (char vowel in vowels)
        {
            Console.Write(vowel + " ");
        }
        Console.WriteLine();
        Console.WriteLine("Index of 'o': " + vowels.IndexOf('o'));


        Console.WriteLine();
        Console.WriteLine("quick .Contains & .Remove()");
        List<int> bin = new List<int> { 1, 0, 0, 1, 1, 1, 0, 0, 0, 1 };

        while (bin.Contains(0))
            bin.Remove(0);

        for (int i = 0; i < bin.Count; i++)
            Console.Write(bin[i]);

        Console.WriteLine();
    }

    static void ListDeclaration()
    {
        Console.WriteLine();
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine("* List Declaration");
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine();

        List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        foreach (int num in numbers)
            Console.Write(num + " ");

        Console.WriteLine();
        Console.WriteLine();
    }

    static void WhatAreLists()
    {
        Console.WriteLine();
        Console.WriteLine("*********************************************************************************************************************");
        Console.WriteLine("* What are Lists"); // requires - using System.Collections.Generic;
        Console.WriteLine("*********************************************************************************************************************");
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