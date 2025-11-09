import torch # import torch before cpp_extension
import cppcuda_tutorial


feats = torch.ones(2)
point = torch.zeros(2)


out = cppcuda_tutorial.trilinear_interpolation(feats, point)

print(out)
