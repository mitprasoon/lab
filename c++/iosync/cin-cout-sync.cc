#include <iostream>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    for (int i = 0; i < 1000000; i++) {
        long n;
        std::cin >> n;
        std::cout << n << '\n';
    }
}
