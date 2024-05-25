using System;

namespace linear_sorts
{
    public class Stack
    {
        private int[] stackArray;
        private int top;
        private long count;
        private int size;

        public uint n_op = 0;

        public long Count { 
            get => count; 
            set {
                count = value;
            } 
        }

        public Stack(int size)
        {
            stackArray = new int[size];
            this.size = size;
            top = -1;
        }

        public int this[int i]
        {
            get
            {
                if (i < -1 || i > top)
                {
                    throw new IndexOutOfRangeException("Index out of range");
                }
                else
                {
                    n_op += 1;
                    Stack temp = new Stack(this.size);

                    n_op += 4;
                    for (int j = top; j > i; j--)
                    {
                        n_op += 2;
                        temp.Push(this.Pop());
                    }

                    n_op += 2;
                    int res = Pop();

                    n_op += 2;
                    this.Push(res);

                    n_op += 1;
                    while (!temp.IsEmpty())
                    {
                        n_op += 2;
                        int val = temp.Pop();
                        n_op += 2;
                        this.Push(val);
                    }

                    return res;
                }
            }
            set
            {
                if (i < 0 || i > top)
                {
                    throw new IndexOutOfRangeException("Index out of range");
                }
                else
                {
                    n_op += 1;
                    Stack temp = new Stack(this.size);

                    n_op += 4;
                    for (int j = top; j > i; j--)
                    {
                        n_op += 2;
                        temp.Push(this.Pop());
                    }

                    n_op += 3;
                    Pop();
                    Push(value);

                    while (!temp.IsEmpty())
                    {
                        n_op += 2;
                        int val = temp.Pop();

                        n_op += 2;
                        this.Push(val);
                    }
                }
            }
        }

        public void Push(int value)
        {
            n_op += 1;
            if (IsFull())
            {
                Console.WriteLine("Stack is full. Cannot push.");
                return;
            }
            n_op += 1;
            count++;
            n_op += 3;
            stackArray[++top] = value;
        }

        public int Pop()
        {
            n_op += 1;
            count--;
            n_op += 2;
            int top_value = stackArray[top];
            n_op += 1;
            stackArray[top] = 0;
            n_op += 1;
            top--;
            return top_value;
        }

        public int Peek()
        {
            if (IsEmpty())
            {
                Console.WriteLine("Stack is empty. Cannot peek.");
                return -1;
            }

            return stackArray[top];
        }

        public bool IsEmpty()
        {
            return Count == 0;
        }

        public bool IsFull()
        {
            n_op += 3;
            return top == stackArray.Length - 1;
        }

        public void Print()
        {
            int[] displayArray = new int[count];
            for (long i = count - 1; i >= 0; i--)
            {
                displayArray[i] = (int)stackArray[i];
            }
            
            for (int i = 0; i < displayArray.Length; i++)
            {
                Console.WriteLine(displayArray[i]);
            }
        }
    }
}