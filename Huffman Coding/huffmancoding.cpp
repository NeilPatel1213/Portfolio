#include <bits/stdc++.h>
#include <queue>
using namespace std;

struct Node
{
    char character;
    int frequency;
    Node *leftChild;
    Node *rightChild;

    Node(char c, int freq) //paramter constructor for struct
    {
            leftChild = NULL;
            rightChild = NULL;
            this->character = c;
            this->frequency = freq;
    }
};

struct compare
{
    bool operator() (Node *left, Node *right) //overload operator so that priority queue can use this compare
    {
        int s = left->frequency > right->frequency;
        return s;
    }
};

priority_queue<Node *, vector<Node *>, compare> minHeap; //create the minHeap using priority queue

void printHuffmanCode(struct Node *root, string output)
{
    if(root == NULL)
        return;
    
    if(root->character != '?') //merged characters = ?
    {
        cout << root->character << " translates to: " << output << "\n";
    }

    printHuffmanCode(root->leftChild, output + "1");
    printHuffmanCode(root->rightChild, output + "0");
} 

void Huffman(char characters[], int frequency[], int numberOfCharacters)
{
    struct Node *lChild;
    struct Node *rChild;
    struct Node *parent;

    for(int i = 0; i < numberOfCharacters; i++) //push the nodes
    {
        minHeap.push(new Node(characters[i], frequency[i])); //each node represents a character and its frequency
    }

    while(minHeap.size() > 1) //keeps merging until everything is condensed under one root, huffman tree
    {
        //compare function should've already sorted the nodes by frequency
        lChild = minHeap.top(); //gives top element
        minHeap.pop();

        rChild = minHeap.top(); //gives top element
        minHeap.pop();

        parent = new Node('?', lChild->frequency + rChild->frequency); //merge

        parent->leftChild = lChild;
        parent->rightChild = rChild;

        minHeap.push(parent); //add the merged node into the huffman tree
    }
}

int main()
{
    char message[] = {'a', 'h', 'e', 'f'};
    int freq[] = {10, 20, 3, 5};
    int size = 4; //number of characters

    Huffman(message, freq, 4);

    string output = "";
    printHuffmanCode(minHeap.top(), output);
}