#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
using namespace std;

class Node
{
    public: 
        Node* next;
        int id;

        Node(int currentID) //constructor
        {
            id = currentID;
            next = nullptr;
        }

        Node() //no name constructor
        {
            id = -1;
            next = nullptr;
        }
};

class Ring
{
    public:
        Node* beginning;
        std::mutex mut;

        Ring() //constructor
        {
            beginning = nullptr;
        }

        void createRing(vector<int> nodesID)
        {
            for(int i = 0; i < nodesID.size(); i++)
            {
                if(beginning == nullptr)
                {
                    beginning = new Node(nodesID.at(i));
                    beginning->next = beginning;
                }
                else
                {
                    Node* newNode = new Node(nodesID.at(i));
                    Node* temp = beginning;

                    //loop around until you get to the beginning of the ring:
                    while(temp->next != beginning)
                        temp = temp->next;
                    
                    temp->next = newNode; //appends the new Node at the end of the ring
                    newNode->next = beginning; //loops back to the beginning of the ring

                }
            }
        }

        void election()
        {
            mut.lock();
            Node* temp = beginning;
            int leaderID = temp->id; //assign leader to start temporarily

            while(true)
            {
                if(temp->id > leaderID)
                    leaderID = temp->id;
                temp = temp->next;

                if(temp == beginning) //once it loops back to the beginning, break the loop
                    break;
            }

            std::cout << "Leader is " << leaderID << std::endl;
            mut.lock();
        }
};

int main()
{
    Ring ring;
    vector<int> ids = {1,2,3,4,5};

    ring.createRing(ids);

    vector<std::thread> threads;

    for(int i = 0; i < ids.size(); i++)
    {
        threads.push_back(std::thread(&Ring::election, &ring));
    }

    for(auto& th : threads)
        th.join();
    
    ring.election();
}