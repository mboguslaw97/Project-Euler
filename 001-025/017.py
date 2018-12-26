ones = ['one', 'two', 'three', 'four', 'five', 'six',  'seven', 'eight', 'nine']
teens = ['ten',  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def sum_lengths(nums):
    return sum(len(x) for x in nums)

ones_sum = sum_lengths(ones)
teens_sum = sum_lengths(teens)
tens_sum = 10*sum_lengths(tens) + 8*ones_sum
hundred_sum = ones_sum + teens_sum + tens_sum
hundreds_sum = 100*ones_sum + 900*len('hundred') + 99*9*len('and') + 9*hundred_sum
result = hundred_sum + hundreds_sum + len('onethousand')
print(result)



