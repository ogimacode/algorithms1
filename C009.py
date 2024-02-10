n = int(input())

fi = 1
fi1 = 0
fi2 = 1
i = 0
while i < n:
    print(fi, end=' ')
    fi = fi1 + fi2
    fi1 = fi2
    fi2 = fi
    i = i + 1