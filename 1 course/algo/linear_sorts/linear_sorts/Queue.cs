using System;


namespace linear_sorts
{
    public class Queue
    {

        private int front = -1; // 1
        private int rear = -1; // 1
        private int count = 0; // 1

        private int capacity;
        private int[] values;

        public ulong N_op;

        public int Count // 2
        {
            get { return count; } // 1
            set
            {
                N_op++;
                count = value; // 1 
            }
        }


        public Queue(int size) // 3
        {
            capacity = size; // 1
            values = new int[size]; // 2
            N_op = 0;
        }


        public void Display() // 7 + n
        {
            for (int i = 0; i < values.Length; i++) // 4 + 3 +
            {
                Console.WriteLine(values[i]); // 1
            }
        }

        public bool IsFull() // 4
        {
            N_op += 2;
            return rear + 1 == capacity; // 4
        }


        public bool IsEmpty() // 3
        {
            N_op+=3;
            return count == 0; // 3
        }

        public void Clear() // 2
        {
            N_op++;
            Array.Clear(values, 0, count); // 1
        }


        public void Enqueue(int item) // 15
        {
            
            if (IsFull()) // 7
            {
                int[] newArray = new int[capacity * 2]; // 4
                values.CopyTo(newArray, 0); // 1
                values = newArray; // 1
                capacity *= 2; // 2
                N_op += 6;
            }

            values[++rear] = item; // 2
            count++; // 1

            N_op += 3;
        }

        public int Dequeue() // 17
        {
            if (this.IsEmpty()) // 7
                throw new Exception("Очередь не заполнена.");

            int value = values[++front]; // 3
            count--; // 1
            N_op += 3;

            N_op += 1;
            if (front == rear) // 1
            {
                front = -1; // 1
                rear = -1; // 1
                Clear(); // 2

                N_op += 2;
            }

            return value; // 1
        }

        public int Get(int index) // 96n + 69
        {
            Queue temp = new Queue(1); // 3


            N_op += 3;
            for (int i = 0; (!IsEmpty()) && (i < index); i++) // 13 + 32n
            {
                N_op += 2;
                temp.Enqueue(Dequeue()); // 15 + 17 = 32
            }

            int ret = Dequeue(); // 18
            N_op++;
            temp.Enqueue(ret); // 16

            N_op += 2;
            for (int i = 0; !IsEmpty(); i++) // 9 + 32n
            {
                N_op += 2;
                temp.Enqueue(Dequeue()); // 32
            }


            N_op += 2;
            for (int i = 0; !temp.IsEmpty(); i++) // 9 + 32n
            {
                N_op += 2;
                Enqueue(temp.Dequeue());
            }

            N_op += temp.N_op;
            return ret; // 1
        }




        public void Set(int x, int idx) // 99n + 62
        {
            N_op += 1;
            Queue temp = new Queue(1); // 3
            

            N_op += 3;
            for (int i = 0; (i < idx) && (!IsEmpty()); i++) // 13 + 32n
            {
                N_op += 3;
                temp.Enqueue(Dequeue());
            }

            N_op += 2;
            Dequeue(); // 17


            temp.Enqueue(x); // 16

            N_op++;
            while (!IsEmpty()) // 35n
                temp.Enqueue(Dequeue());

            N_op += 2;
            for (int i = 0; !temp.IsEmpty(); i++) // 13 + 32n
            {
                N_op += 2;
                Enqueue(temp.Dequeue());
                
            }

            N_op += temp.N_op;

        }

        public int this[int index]
        {
            get { 
                return Get(index); 
            }
            set { 
                Set(value, index); 
            }
        }
    }
}