/**
 * Algorithm: Binary Search
 * Description: Efficient search algorithm for sorted arrays
 * Time Complexity: O(log n)
 * Space Complexity: O(1) iterative, O(log n) recursive
 */

#include <iostream>
#include <vector>
using namespace std;

// Iterative binary search
int binarySearchIterative(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Not found
}

// Recursive binary search
int binarySearchRecursive(const vector<int>& arr, int target, int left, int right) {
    if (left > right) {
        return -1; // Not found
    }
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid;
    } else if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid + 1, right);
    } else {
        return binarySearchRecursive(arr, target, left, mid - 1);
    }
}

int main() {
    vector<int> arr = {2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78};
    
    int target = 23;
    cout << "Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    
    cout << "Searching for " << target << endl;
    
    int result1 = binarySearchIterative(arr, target);
    if (result1 != -1) {
        cout << "Iterative: Found at index " << result1 << endl;
    } else {
        cout << "Iterative: Not found" << endl;
    }
    
    int result2 = binarySearchRecursive(arr, target, 0, arr.size() - 1);
    if (result2 != -1) {
        cout << "Recursive: Found at index " << result2 << endl;
    } else {
        cout << "Recursive: Not found" << endl;
    }
    
    return 0;
}
