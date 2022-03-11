%% Se abre la img
clear
clc
I = imread('lenna.png');
imshow(I)
%% Histograma con la función de matlab
[c, bin] = imhist(I);
figure
imhist(I); % o solo histogram(I)
xlim([0 255]);
title('Histograma de matlab (imhist)')
%% Histograma de una img (mxnx1) desde cero
[ii,kk] = size(I);
y = zeros(256,1);

for i = 1:ii
    for k = 1:kk
        % es +1 por que matlab piensa que esta bien contar desde 1
        y(I(i,k)+1) = y(I(i,k)+1) + 1;
    end
end

% el histograma ya esta en y
% ahora solo se grafica

figure
subplot(3,2,1)
bar(y, 'red');
xlim([0 255]);
title('Mi histograma')

subplot(3,2,2)
bar(c)
xlim([0 255]);
title('imhist')

subplot(3,2,[3,4])
hold on
bar(c)
plot(y, 'red','LineWidth',2)
xlim([0 255]);
legend({'imhist de matlab','Mi histograma'},'Location','southwest')
hold off

% comprobando que este bien
delta = c-y;
subplot(3,2,[5,6])
bar(delta)
title('Diferencia entre ambos histogramas')

%% Comprobando con el toolbox de Peter Corke
% hay que instalar el rvc del wen Peter (y correr startup_rvc.m)
%{

figure
idisp(I)
%figure
[h,x] = ihist(I);
%bar(x,h);
delta2 = h-y;

figure
subplot(3,2,1)
bar(y, 'red');
xlim([0 255]);
title('Mi histograma')

subplot(3,2,2)
bar(h)
xlim([0 255]);
title('ihist de vision toolbox de Peter Corke')

subplot(3,2,[3,4])
hold on
bar(h)
plot(y, 'red','LineWidth',2)
xlim([0 255]);
legend({'imhist de matlab','Mi histograma'},'Location','southwest')
hold off

% comprobando que este bien
subplot(3,2,[5,6])
bar(delta2)
title('Diferencia entre ambos histogramas')
%}