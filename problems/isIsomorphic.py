def isIsomorphic(s: str, t: str) -> bool:
    char_index_s = {}
    char_index_t = {}
    for i in range(len(s)):
        if s[i] not in char_index_s:
            char_index_s[s[i]] = i
        if t[i] not in char_index_t:
            char_index_t[t[i]] = i

        print(
            char_index_s,
            char_index_s[s[i]],
            "|",
            char_index_t,
            char_index_t[t[i]],
            "|",
        )
        if char_index_s[s[i]] != char_index_t[t[i]]:
            return False

    return True


# s = "e g g"
# t = "a b b"
# ch_ind_s ={}, ch_ind_t ={}
# s = "e g g"
# t = "a b b"
#      i
# ch_ind_s ={e:0}, ch_ind_t ={a:0}
# s = "e g g"
# t = "a b b"
#        i
# ch_ind_s ={e:0,g:1}, ch_ind_t ={a:0,b:1}
# s = "e g g"
# t = "a b b"
#          i
# ch_ind_s ={e:0,g:1}, ch_ind_t ={a:0,b:1}


s = "egg"
t = "adb"
print(isIsomorphic(s, t))
for c1, c2 in zip(s, t):
    print(c1, c2)
# s = "e g g"
# t = "a d b"
# ch_ind_s ={}, ch_ind_t ={}
# s = "e g g"
# t = "a d b"
#      i
# ch_ind_s ={e:0}, ch_ind_t ={a:0}
# s = "e g g"
# t = "a d b"
#        i
# ch_ind_s ={e:0,g:1}, ch_ind_t ={a:0,d:1}
# s = "e g g"
# t = "a d b"
#          i
# ch_ind_s ={e:0,g:1}, ch_ind_t ={a:0,d:1,b:2}