using System;

namespace CS_BeyondBasics
{
    /// <summary>
    /// Summary description for Class1
    /// </summary>
    public class StructuresAndFileHandling
    {
        /// <summary> Method MoreErrorHandling()
        /// <para>
        /// </para>
        /// </summary>
        public void MoreErrorHandling()
        {
            Console.WriteLine();
            Console.WriteLine("*****************************************************************************************************");
            Console.WriteLine("* More Error Handling \n*  - DivideByZeroException\n*  - FileNotFoundException\n*  - KeyNotFoundException\n*  - IndexOutOfRangeException");
            Console.WriteLine("*****************************************************************************************************");
            Console.WriteLine();

            int[] numbers = { 1, 2, 5, 7, 9 };
            var numberNames = new Dictionary<int, string>();

            numberNames.Add(1, "One");
            numberNames.Add(2, "Two");
            numberNames.Add(5, "Five");
            numberNames.Add(9, "Nine");

            int i = 0;
            while (true)
            {
                try
                {
                    int key = numbers[i];
                    Console.WriteLine($"{key} is {numberNames[key]}");
                    i++;
                }
                catch (IndexOutOfRangeException)
                {
                    Console.WriteLine("IndexOutOfRangeException");
                    break;
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine("KeyNotFoundException");
                    numberNames.Add(7, "Seven");
                }
            }
        }

        /// <summary> Method ErrorHandling()
        /// <para>
        /// A runtime error is an error which occurs while prgram is running
        /// </para>
        /// </summary>
        public void ErrorHandling()
        {
            Console.WriteLine();
            Console.WriteLine("*****************************************************************************************************");
            Console.WriteLine("* Error Handling");
            Console.WriteLine("*****************************************************************************************************");
            Console.WriteLine();

            // try{} catch{}
            // finally{} - optional
            try
            {
                new StreamWriter("C:/a/random/path/that/does/not/exist.txt");
            }
            catch (Exception error)
            {
                Console.WriteLine(error.Message);
            }

            // Division by zero
            Console.WriteLine();
            try
            {
                int a = 100;
                int b = 0;
                int result = a / b;
            }
            catch
            {
                Console.WriteLine("ERROR: Division by Zero.");
            }

            // Invalid index of array or list
            Console.WriteLine();
            try
            {
                var exampleArray = new int[10];
                Console.WriteLine(exampleArray[20]);
            }
            catch
            {
                Console.WriteLine("ERROR: The array index is out of bounds.");
            }

            // Key not found
            Console.WriteLine();
            try
            {
                Dictionary<string, string> myDict = new Dictionary<string, string>
            {
                { "key1", "value1" }
            };
                Console.WriteLine(myDict["key2"]);
            }
            catch
            {
                Console.WriteLine("Error: Key not found");
            }

            // "finally" block
            Console.WriteLine();
            try
            {
                Dictionary<string, string> myDict = new Dictionary<string, string>
            {
                { "key1", "value1" }
            };
                Console.WriteLine(myDict["key2"]);
            }
            catch
            {
                Console.WriteLine("Error: Key not found");
            }
            finally // execute "finally" code regardless if exception is thrown or not
            {
                Console.WriteLine("This line will show after the error");
            }
        }

        /// <summary> Method UsingStreamWriter()
        /// <para></para>
        /// </summary>
        public void UsingStreamWriter()
        {
            Console.WriteLine();
            Console.WriteLine("*********************************************************************************************************************");
            Console.WriteLine("* StreamReader()");
            Console.WriteLine("*********************************************************************************************************************");
            Console.WriteLine();

            // StreamWriter has a second value 'append' set to false by default
            var tempFile = new StreamWriter("C:/Users/le-ni/OneDrive/Desktop/tempFile_01");
            tempFile.WriteLine("This is some new text.");
            tempFile.WriteLine("This is the next line.");
            tempFile.WriteLine("Another line.");
            tempFile.Close();

            // setting append to true appends to file and does not overwrite
            var tempFile2 = new StreamWriter("C:/Users/le-ni/OneDrive/Desktop/tempFile_01", true);
            tempFile2.WriteLine("Yet another line.");
            tempFile2.Close();
        }

        /// <summary> Method ReadingFilesUsingFileMethods()
        /// <para>
        /// This method is to demonstrate reading files using methods
        /// </para>
        /// </summary>
        public void ReadingFilesUsingFileMethods()
        {
            Console.WriteLine();
            Console.WriteLine("*********************************************************************************************************************");
            Console.WriteLine("* Reading file");
            Console.WriteLine("*********************************************************************************************************************");
            Console.WriteLine();

            // .ReadAllText() handles openeing and closing file internally ie you don't need to call .Close() on the file
            string tempText = File.ReadAllText("C:/Users/le-ni/OneDrive/Desktop/temp.file");
            Console.WriteLine(tempText);

        }

        /// <summary> Method ReadingFilesUsingStreamReader()
        /// <para>
        /// This method is to demonstrate reading files using StreamReader()
        /// </para>
        /// </summary>
        public void ReadingFilesUsingStreamReader()
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

        public void WhatAreDictionaries()
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

        public void ListMethods()
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

        public void ListDeclaration()
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

        public void WhatAreLists()
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
}