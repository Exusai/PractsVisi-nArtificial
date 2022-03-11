clear
clc

% Imagen
A = imread('ipn.png');
figure
imshow(A)
A = rgb2gray(A);
A = double(A);

% Filtro laplaciano
filtro = [-1 -1 -1;-1 8 -1;-1 -1 -1];

% Mi implementación:
% se implmenta convolución con kernel de 3x3 y padding 'same'
% osea se añaden 2 columnas/filas de ceros a los bordes de la img
% si se usara un kernel de 5x5 se añadirían 4 filas/columnas de 0   
A = padarray(A,2, 'both');
A = padarray(A,[0,2], 'both');
[j, k] = size(A);
filtrada = zeros(j,k);

for h = 2:j-1
    for i = 2:k-1
        filtrada(h,i) = sum(sum(filtro .* A(h-1:h+1, i-1:i+1)));
        %filtrada(h,i) = sum(sum(A(h-1:h+1, i-1:i+1) * filtro));
    end
end
%filtro = [1 0 -1;0 0 0;-1 0 1];

% Implementación de matlab
matlabConv = conv2(A,filtro, 'same');
dif = filtrada - matlabConv;
error = sum(sum(dif))

dif = uint8(dif);
imgMat = uint8(matlabConv);
myImg = uint8(filtrada);

% Comparando
figure
subplot(3,2,[1,2])
imshow(myImg)
title('Mi Implementación')

subplot(3,2,[3,4])
imshow(imgMat);
title('Conv2 de Matlab')

subplot(3,2,[5,6])
imshow(imgMat-myImg)
title('Diferencia entre ambas convoluciones')

