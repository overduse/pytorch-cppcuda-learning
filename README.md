# PyTorch Cpp-Extension Tutorial

This is a simple template project for a PyTorch C++ extension. It implements a basic `trilinear_interpolation` function to demonstrate how to set up and build the development environment.

The main focus is on a clean project structure and the build process.

## File Structure

```
.
├── README.md
├── interpolation.cpp  # C++ source code
├── setup.py           # Python setuptools build script
└── test.py            # Python script for testing
```

## Prerequisites

*   Python `3.9`
*   PyTorch
*   A C++ compiler (e.g., g++ or clang)
*   Environment: WSL2 (Ubuntu 22.04)
*   [Conda](https://docs.conda.io/en/latest/) (Recommended) for managing the environment.

## Installation and Build

1.  **Clone the repository**
    ```bash
    git clone https://github.com/overduse/pytorch-cppcuda-learning.git
    cd pytorch-cppcuda-learning
    ```

2.  **Create and activate a Conda environment**
    We'll create a new environment named `cppcuda` to isolate dependencies.
    ```bash
    conda create -n cppcuda python=3.9
    conda activate cppcuda
    ```

3.  **Install PyTorch**
    With the environment activated, install PyTorch. This project was set up using the command for CUDA 12.6:
    ```bash
    pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
    ```

4.  **Build the C++ Extension**
    For development, it's convenient to build the extension in-place. This creates the shared library (`.so` or `.pyd`) directly in the project directory, making it immediately importable.
    ```bash
    python setup.py build_ext --inplace
    ```
    After a successful build, you will find a `build` directory and a shared library file (e.g., `cppcuda_tutorial.cpython-39-x86_64-linux-gnu.so`) in your project root.

## How to Run

Run the `test.py` script to call the compiled C++ function.
```bash
python test.py
```
If everything is set up correctly, it will print a Torch tensor:
```
tensor([1., 1.])
```
