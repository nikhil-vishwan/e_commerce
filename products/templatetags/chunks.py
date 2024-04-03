# from django import template

# register = template.Library()


# @register.filter(name='chunks')
# def chunks(list_data,chunk_size):
#     chunk=[]
#     i=0
#     for data in list_data:
#         chunk.append(data)
#         i=i+1
#         if i==chunk_size:
#             yield row
#             row=[]
#     if chunk:  
#         yield chunk



from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk = []
    i = 0
    for data in list_data:
        chunk.append(data)
        i = i + 1
        if i == chunk_size:
            yield chunk
            chunk = []  # Reset chunk for the next iteration
            i = 0       # Reset counter
    if chunk:
        yield chunk


