import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width= max_width) 
  
    word = wrapper.wrap(text= string) 

    if max_width<=len(string):
        return "\n".join(word)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)