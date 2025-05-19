using System;
using System.Diagnostics;
using System.Text;

namespace linear_sorts
{



    public class Program
    {

        public static ulong BubbleSort(Queue queue) // 
        {
            ulong sort_n_op = 3;
            for (int i = 0; i < queue.Count - 1; i++) // 5 + n*(
            {
                sort_n_op += 6;
                for (int j = 0; j < queue.Count - i - 1; j++) // 7 + n*(
                {
                    sort_n_op += 3;
                    if (queue[j] > queue[j + 1]) // 576n + 420
                    {
                        sort_n_op += 5;
                        var tempVar = queue[j]; 
                        queue[j] = queue[j + 1]; 
                        queue[j + 1] = tempVar; 
                    }
                }
            }
            return sort_n_op;
        }


        static void Main(string[] args)
        {

            Console.InputEncoding = Encoding.UTF8;
            Console.OutputEncoding = Encoding.UTF8;

            Stopwatch stopwatch = new Stopwatch();
            Random rand = new Random();

            uint QUEUE_SIZE = 100;


            for (int i = 0; i < 10; QUEUE_SIZE += 50)
            {
                Queue queue = new Queue((int)QUEUE_SIZE);

                for (int j = 0; j < QUEUE_SIZE; j++)
                    queue.Enqueue(rand.Next(-10000, 10000));

                stopwatch.Reset();


                stopwatch.Start();

                ulong sort_n_op = BubbleSort(queue);

                stopwatch.Stop();

                Console.WriteLine($"Кол-во отсортированных элементов {QUEUE_SIZE}");
                Console.WriteLine("N_op очереди: " + queue.N_op);
                Console.WriteLine("N_op сортировки: " + sort_n_op);
                Console.WriteLine(queue.N_op + sort_n_op);

                Console.WriteLine("Sort time : " + stopwatch.Elapsed.Seconds + ":" + stopwatch.Elapsed.Milliseconds + "\n");

            }
            
            



            Console.ReadKey();
        }

        
    }
}
