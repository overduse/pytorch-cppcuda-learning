# PyTorch C++/CUDA Extension Tutorial

This project is a simple template for building a PyTorch extension that uses both C++ and CUDA. It implements a basic `trilinear_interpolation` function to demonstrate a clean project structure and the complete development and build process.

## File Structure

```
.
├── include
│   └── utils.h              # Header file for function declarations
├── interpolation.cpp        # C++ interface code (binds to Python)
├── interpolation_kernel.cu  # CUDA kernel implementation
├── setup.py                 # Python setuptools build script
├── test.py                  # Python script for testing
└── README.md
```

## Prerequisites

*   **Python**
*   **NVIDIA CUDA Toolkit**
*   **PyTorch**
*   **Build Tools**: A C++ compiler (e.g., `g++`, `clang`, or MSVC) and `ninja`.
*   [**Conda**](https://docs.conda.io/en/latest/) is highly recommended for managing dependencies in an isolated environment.

### Key Requirement: CUDA Version Consistency

For a successful compilation, it is **critical** that the version of the **NVIDIA CUDA Toolkit** installed on your system matches the CUDA version that your **PyTorch** was built with.

*   **System `nvcc`**: This is the CUDA compiler found by your system. You can check its version by running `nvcc --version` in your terminal.
*   **PyTorch's CUDA Runtime**: This is the version of the CUDA libraries that PyTorch was compiled against.

If these two versions do not match, you will likely encounter compilation errors.

## Installation and Build

1.  **Clone the repository**
    ```bash
    git clone https://github.com/overduse/pytorch-cppcuda-learning.git
    cd pytorch-cppcuda-learning
    ```

2.  **Set up your Python Environment**
    It is highly recommended to use a virtual environment. The following commands use Conda to create an environment named `cppcuda`.
    ```bash
    conda create -n cppcuda python
    conda activate cppcuda
    ```

3.  **Install Dependencies (PyTorch & Ninja)**
    Install a version of PyTorch that matches your system's CUDA Toolkit. For example, if your `nvcc --version` shows **CUDA 11.8**, you must install the PyTorch build for CUDA 11.8.

    ```bash
    # Example for CUDA 11.8. Find the correct command for your setup on the PyTorch website.
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
    
    # Install the Ninja build system, which is required by PyTorch for extensions
    pip install ninja
    ```

4.  **Verify Your Environment**
    Before building, run the following Python code to ensure your environment is correctly configured:
    ```python
    import torch
    import torch.utils.cpp_extension

    # Check PyTorch version
    print(f"PyTorch Version: {torch.__version__}")

    # Check PyTorch's compiled CUDA version. This MUST match your system's nvcc version.
    print(f"PyTorch CUDA Version: {torch.version.cuda}")

    # Check if your GPU is visible to PyTorch
    print(f"Is CUDA available: {torch.cuda.is_available()}")

    # Check the CUDA path PyTorch's extension builder will use.
    # This should point to your system's CUDA Toolkit installation.
    print(f"CUDA_HOME: {torch.utils.cpp_extension.CUDA_HOME}")
    ```
    Ensure that the `PyTorch CUDA Version` reported here matches the output of `nvcc --version` in your terminal.

5.  **Build the C++/CUDA Extension**
    Build the extension in-place. This creates the shared library (`.so` on Linux, `.pyd` on Windows) directly in the project directory, making it immediately importable.
    ```bash
    python setup.py build_ext --inplace
    ```
    After a successful build, a `build/` directory and a shared library file (e.g., `cppcuda_tutorial.cpython-39-x86_64-linux-gnu.so`) will appear in your project root.

## How to Run

Run the `test.py` script to import and execute the compiled C++/CUDA function.
```bash
python test.py
```
