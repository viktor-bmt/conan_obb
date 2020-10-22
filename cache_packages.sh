#!/bin/bash
conan export ./obb ar/stable
conan create ./reader ar/stable
