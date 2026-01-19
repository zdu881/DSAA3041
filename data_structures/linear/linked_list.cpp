/**
 * Data Structure: Singly Linked List
 * Description: Basic implementation of a singly linked list
 * 
 * Operations:
 * - insert(): O(1) at head, O(n) at tail
 * - delete(): O(1) at head, O(n) elsewhere
 * - search(): O(n)
 */

#include <iostream>
using namespace std;

template<typename T>
class Node {
public:
    T data;
    Node* next;
    
    Node(T val) : data(val), next(nullptr) {}
};

template<typename T>
class LinkedList {
private:
    Node<T>* head;
    int size;
    
public:
    LinkedList() : head(nullptr), size(0) {}
    
    // Insert at the beginning
    void insertFront(T val) {
        Node<T>* newNode = new Node<T>(val);
        newNode->next = head;
        head = newNode;
        size++;
    }
    
    // Insert at the end
    void insertBack(T val) {
        Node<T>* newNode = new Node<T>(val);
        if (!head) {
            head = newNode;
        } else {
            Node<T>* curr = head;
            while (curr->next) {
                curr = curr->next;
            }
            curr->next = newNode;
        }
        size++;
    }
    
    // Delete by value
    bool deleteValue(T val) {
        if (!head) return false;
        
        if (head->data == val) {
            Node<T>* temp = head;
            head = head->next;
            delete temp;
            size--;
            return true;
        }
        
        Node<T>* curr = head;
        while (curr->next && curr->next->data != val) {
            curr = curr->next;
        }
        
        if (curr->next) {
            Node<T>* temp = curr->next;
            curr->next = curr->next->next;
            delete temp;
            size--;
            return true;
        }
        
        return false;
    }
    
    // Display the list
    void display() {
        Node<T>* curr = head;
        while (curr) {
            cout << curr->data << " -> ";
            curr = curr->next;
        }
        cout << "NULL" << endl;
    }
    
    int getSize() { return size; }
    
    ~LinkedList() {
        while (head) {
            Node<T>* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    LinkedList<int> list;
    
    list.insertFront(3);
    list.insertFront(2);
    list.insertFront(1);
    list.insertBack(4);
    list.insertBack(5);
    
    cout << "List: ";
    list.display();
    
    list.deleteValue(3);
    cout << "After deleting 3: ";
    list.display();
    
    cout << "Size: " << list.getSize() << endl;
    
    return 0;
}
