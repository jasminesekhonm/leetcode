class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        
        for email in emails:
            username, domainname = email.split("@")
            filtered_username = ""
            for char in username:
                if char == '.':
                    continue 
                elif char == '+':
                    break 
                filtered_username = filtered_username + char 
            new_add = filtered_username + '@' + domainname 
            if new_add not in res:
                res.append(new_add)
        return len(res)
                
        
