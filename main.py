import torch
from bitpacking import pack_bits

nums = torch.randn(4)
bins = [i for i in range(16)]

S = (max(nums)-min(nums))/(max(bins)-min(bins))
Z = torch.round(min(bins)-(min(nums)/S))

nums_q = torch.round((nums/S)+Z).to(torch.uint8)
nums_dq = S*(nums_q-Z)

quantization_error = ((nums-nums_dq)**2).mean()

print(f"Original nums: {nums}")
print(f"Number of bins: {len(bins)}")
print(f"Scaling factor: {S}")
print(f"Zero point: {Z}")
print(f"\nQuantized nums: {nums_q}")
print(f"Dequantized nums: {nums_dq}")
print(f"Quantization error: {quantization_error:.3f}")


num1 = nums_q[0]
num2 = nums_q[1]
num3 = nums_q[2]
num4 = nums_q[3]

# print(f"{num1:08b}")
# print(f"{num2:08b}")
# print(f"{num3:08b}")
# print(f"{num4:08b}")

packed_1 = pack_bits(num1, num2)
packed_2 = pack_bits(num3, num4)

final_packed_tensor = torch.tensor([packed_1,packed_2], dtype=torch.uint8)
print(f"Packed bits tensor: {final_packed_tensor}")
print(f"\n\n\n************************************************************")
print(f"Original size of tensor: {32*len(nums)} bits")
print(f"Quantized tensor size: {8*len(nums_q)} bits")
print(f"Packed tensor size: {8*len(final_packed_tensor)} bits")

print(f"\nOriginal tensor: {nums}")
print(f"Dequantized tensor: {nums_dq}")
print(f"Quantization error: {quantization_error:.3f}")
