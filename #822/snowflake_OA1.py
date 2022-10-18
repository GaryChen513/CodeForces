def stringPattern(wordLen, maxVowel):
    dp = [-1] * (wordLen + 1)
    mod = 1000000007
    for numNonVowel in range(wordLen + 1):
        numVowel = wordLen - numNonVowel
        dp[numNonVowel] = (5**(numVowel) * (21**numNonVowel) * (wordLen - numVowel + 1)) - sum(dp[:numNonVowel])

    print(dp)
    return sum(dp[wordLen - maxVowel:])

wordLen = 4
maxVowel = 1
print(stringPattern(wordLen, maxVowel))


