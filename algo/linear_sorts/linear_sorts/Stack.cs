using System;

namespace linear_sorts
{
    public class Stack
    {
        private int[] stackArray;
        private int top;
        private int count;

        public int Count { 
            get => count; 
            set {
                count = value;
            } 
        }

        public Stack(int size)
        {
            stackArray = new int[size];
            top = -1;
        }

        public int this[int i]
        {
            get
            {
                if (i < 0 || i > top)
                {
                    throw new IndexOutOfRangeException("Index out of range");
                }
                return stackArray[i];
            }
            set
            {
                if (i < 0 || i > top)
                {
                    throw new IndexOutOfRangeException("Index out of range");
                }
                stackArray[i] = value;
            }
        }

        public void Push(int value)
        {
            if (IsFull())
            {
                Console.WriteLine("Stack is full. Cannot push.");
                return;
            }
            count++;
            stackArray[++top] = value;
        }

        public int Pop()
        {
            if (IsEmpty())
            {
                Console.WriteLine("Stack is empty. Cannot pop.");
                return -1;
            }
            count--;
            return stackArray[top--];
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
            return top == -1;
        }

        public bool IsFull()
        {
            return top == stackArray.Length - 1;
        }

        public void Print()
        {
            int[] displayArray = new int[count];
            for (int i = count - 1; i >= 0; i--)
            {
                displayArray[i] = stackArray[i];
            }
            
            for (int i = 0; i < displayArray.Length; i++)
            {
                Console.WriteLine(displayArray[i]);
            }
        }
    }
}