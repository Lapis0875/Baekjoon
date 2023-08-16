#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

/**
 * @brief 두 문자열 변수의 값을 바꾼다.
 * 
 * @param a 변수 1
 * @param b 변수 2
 */
inline void swap(string& a, string& b)
{   
    cout << "swap(" << a << "," << b << ")" << endl;
    string temp = a;
    a = b;
    b = temp;
}


/**
 * @brief 두 문자열을 비교한 결과를 반환한다.
 * 
 * @param a 문자열 a
 * @param b 문자열 b
 * @return int a가 더 짧거나, 사전순으로 앞서면 -1, 같으면 0, 뒤면 1
 */
int compare(const string& a, const string& b)
{
    const int a_len = a.length(), b_len = b.length();
    const int min_len = a.length() < b.length() ? a.length() : b.length();
    int i = 0;

    if (a_len != b_len)
        return a_len < b_len ? -1 : 1;
    while (i < min_len)
    {
        if (a[i] < b[i])
            return -1;
        else if (a[i] > b[i])
            return 1;
    }
    return 0;
}

int compare_cap(const string& a, const string& b)
{
    int res = compare(a, b);

    cout << "compare(" << a << "," << b << ") = " << res << endl;

    return res;
}

void merge(vector<string> vec, int low, int mid, int high)
{
    cout << "merge(vec, " << low << "," << mid << "," << high << "))" << endl;
    vector<string> sorted;
    int i = low, j = mid + 1, k = 0, res = 0;

    while (i <= mid && j <= high)
    {
        res = compare_cap(vec[i], vec[j]);
        if (res < 0)
            sorted[k++] = vec[i++];
        else if (res > 0)
            sorted[k++] = vec[j++];
        else
        {
            cout << "erase duplicate!" << endl;
            vec.erase(vec.begin() + i);
        }
    }

    while (i <= mid)
        sorted[k++] = vec[i++];
    
    while (j <= high)
        sorted[k++] = vec[j++];
    
    for (int idx = 0, k = 0; idx <= high; idx++, k++)
        vec[idx] = sorted[k];
}

void mergesort(vector<string> vec, int low, int high)
{
    cout << "Start mergesort(vec, " << low << "," << high << ")" << endl;
    if (low >= high)
        return;
    int mid = (low + high) / 2;
    mergesort(vec, low, mid);
    mergesort(vec, mid + 1, high);
    merge(vec, low, mid, high);
    cout << "End mergesort(vec, " << low << "," << high << ")" << endl;
}

inline void print_vec(vector<string> vec, int chunk_size)
{
    string str;

    for (int i = 0, c_idx = 0; i < vec.size(); i++, c_idx++)
    {
        str.append(vec[i] + "\n");
        if (c_idx == chunk_size)
        {
            puts(str.c_str());
            str.empty();
            c_idx = 0;
        }
    }
    puts(str.c_str());
    str.empty();
}

int main(void)
{
    int size;
    cin >> size;
    vector<string> vec;
    string str;

    for (int i = 0; i < size; i++)
    {
        cin >> str;
        vec.push_back(str);
    }
    cout << "--" << endl;

    mergesort(vec, 0, size - 1);
    for (int i = 0; i < size; i++)
        cout << vec[i] << endl;
    // print_vec(vec, 100);
    return 0;
}
