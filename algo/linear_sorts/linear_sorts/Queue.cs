using System;


namespace linear_sorts
{
    public class Queue
    {

        private int front = -1;
        private int rear = -1;
        private int count = 0;

        private int capacity;
        private int[] values;

        public int N_op;

        public int Count
        {
            get { return count; }
            set
            {
                N_op++;
                count = value;
            }
        }


        public Queue(int size)
        {
            capacity = size;
            values = new int[size];
            N_op = 0;
        }


        public void Display()
        {
            for (int i = 0; i < values.Length; i++)
            {
                Console.WriteLine(values[i]);
            }
        }

        public bool IsFull()
        {
            N_op += 2;
            return rear + 1 == capacity;
        }


        public bool IsEmpty()
        {
            N_op++;
            return count == 0;
        }

        public void Clear()
        {
            N_op++;
            Array.Clear(values, 0, count);
        }



        public int Peek()
        {
            if (IsEmpty())
                throw new Exception("Очередь не заполнена.");

            N_op += 2;
            int value = values[front + 1];

            return value;
        }


        public void Enqueue(int item)
        {

            if (IsFull())
            {
                int[] newArray = new int[capacity * 2];
                values.CopyTo(newArray, 0);
                values = newArray;
                capacity *= 2; // realloc if full
                N_op += 6;
            }

            values[++rear] = item;
            count++;

            N_op += 3;
        }

        public int Dequeue()
        {
            if (this.IsEmpty())
                throw new Exception("Очередь не заполнена.");

            int value = values[++front];
            count--;
            N_op += 3;

            N_op += 1;
            if (front == rear)
            {
                front = -1;
                rear = -1;
                Clear();

                N_op += 2;
            }

            return value;
        }

        public int Get(int index)
        {
            Queue temp = new Queue(1);


            N_op += 3;
            for (int i = 0; (!IsEmpty()) && (i < index); i++)
            {
                N_op += 2;
                temp.Enqueue(Dequeue());
            }

            int ret = Dequeue();
            N_op++;
            temp.Enqueue(ret);

            N_op += 2;
            for (int i = 0; !IsEmpty(); i++)
            {
                N_op += 2;
                temp.Enqueue(Dequeue());
            }


            N_op += 2;
            for (int i = 0; !temp.IsEmpty(); i++)
            {
                N_op += 2;
                Enqueue(temp.Dequeue());
            }

            N_op += temp.N_op;
            return ret;
        }




        public void Set(int x, int idx)
        {
            N_op += 1;
            Queue temp = new Queue(1);
            

            N_op += 3;
            for (int i = 0; (i < idx) && (!IsEmpty()); i++)
            {
                N_op += 3;
                temp.Enqueue(Dequeue());
            }

            N_op += 2;
            Dequeue();


            temp.Enqueue(x);

            N_op++;
            while (!IsEmpty())
                temp.Enqueue(Dequeue());

            N_op += 2;
            for (int i = 0; !temp.IsEmpty(); i++)
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