clear;
close all;

addpath('../data/simData/')
addpath('../data/output/')

lena = imread("Lena.png");
figure; imagesc(lena)
colorbar

lenaGrayScale = imread("LenaGrayScale.png");
figure; imagesc(lenaGrayScale)
colorbar
colormap gray

figure;
histogram(lenaGrayScale)

gradientPDDO = table2array(readtable("gradientPDDO.csv"));
gradientPDDO = abs(gradientPDDO./max(abs(gradientPDDO(:))));
figure;
imagesc(abs(gradientPDDO))
colormap gray
colorbar
title('PDDO Gradient')

fuzzyPDDOGradient = table2array(readtable("fuzzyPDDOGradient.csv"));
fuzzyPDDOGradient = abs(fuzzyPDDOGradient./max(abs(fuzzyPDDOGradient(:))));
figure;
imagesc(abs(fuzzyPDDOGradient))
colormap gray
colorbar
title('Fuzzy PDDO Gradient')

fuzzyPDDOGradient2 = table2array(readtable("fuzzyPDDOGradient2.csv"));
fuzzyPDDOGradient2 = abs(fuzzyPDDOGradient2./max(abs(fuzzyPDDOGradient2(:))));
figure;
imagesc(abs(fuzzyPDDOGradient2))
colormap gray
colorbar
title('Fuzzy PDDO Gradient 2')

laplacianPDDO = table2array(readtable("laplacianPDDO.csv"));
laplacianPDDO = abs(laplacianPDDO./max(abs(laplacianPDDO(:))));
% laplacianPDDO(laplacianPDDO<.15)=0;
% laplacianPDDO(laplacianPDDO~=0)=1;
figure;
imagesc(laplacianPDDO)
colormap gray
colorbar
title('PDDO Laplacian')

fuzzyPDDOLaplacian = table2array(readtable("fuzzyPDDOLaplacian.csv"));
fuzzyPDDOLaplacian = abs(fuzzyPDDOLaplacian./max(abs(fuzzyPDDOLaplacian(:))));
figure;
imagesc(abs(fuzzyPDDOLaplacian))
colormap gray
colorbar
title('Fuzzy PDDO Laplacian')

fuzzyPDDOLaplacian2 = table2array(readtable("fuzzyPDDOLaplacian2.csv"));
fuzzyPDDOLaplacian2 = abs(fuzzyPDDOLaplacian2./max(abs(fuzzyPDDOLaplacian2(:))));
figure;
imagesc(abs(fuzzyPDDOLaplacian2))
colormap gray
colorbar
title('Fuzzy PDDO Laplacian 2')


DGradient = table2array(readtable("DGradient.csv"));
%DGradient = abs(DGradient.'./max(abs(DGradient(:))));
DGradient = DGradient.';
figure;
imagesc(abs(DGradient))
colormap gray
colorbar
title('D Fuzzy Gradient')

figure; histogram(DGradient)

DLaplacian = table2array(readtable("DLaplacian.csv"));
DLaplacian = DLaplacian.';
%DLaplacian = abs(DLaplacian.'./max(abs(DLaplacian(:))));
figure;
imagesc(abs(DLaplacian))
colormap gray
colorbar
title('D Fuzzy Laplacian')

figure; histogram(DLaplacian)



gradientPDDO = table2array(readtable("gradientPDDO.csv"));
gradientPDDO = gradientPDDO./max(gradientPDDO(:));
%gradientJustPDDO = gradientJustPDDO.*255;
gradientPDDO(gradientPDDO<0.06) = 0;
gradientPDDO(gradientPDDO~=0)=1;

figure; imagesc(abs(gradientPDDO(3:end-2,3:end-2)));
colormap gray
colorbar

se = strel('disk',1);

figure; imagesc(bwperim(imerode(abs(gradientPDDO(3:end-2,3:end-2)),se)));
colormap gray
colorbar



figure; imagesc(bwperim(abs(gradientPDDO(3:end-2,3:end-2))));
colormap gray
colorbar


figure; imagesc(edge(lenaGrayScale,"Sobel"))
colormap gray;
colorbar


figure;
histogram(gradientPDDO)

gradientFuzzyPDDO = table2array(readtable("gradientFuzzyPDDO.csv"));
figure; imagesc(reshape(abs(gradientFuzzyPDDO),[512 512]).');
colormap gray
colorbar
title('1')
figure;
histogram(gradientFuzzyPDDO)
title('1')
gradientFuzzyPDDO2 = table2array(readtable("gradientFuzzyPDDO2.csv"));
figure; imagesc(reshape(abs(gradientFuzzyPDDO2),[512 512]).');
colormap gray
colorbar
title('2')
figure;
histogram(gradientFuzzyPDDO2)
title('2')


gradientFuzzyPDDONotCenter = table2array(readtable("gradientFuzzyPDDONotCenter.csv"));
figure; imagesc(reshape(abs(gradientFuzzyPDDONotCenter),[512 512]).');
colormap gray
colorbar

figure;
histogram(gradientFuzzyPDDONotCenter)


figure; imagesc(edge(lenaGrayScale,"Sobel"))
colormap gray;
colorbar

triangularMembershipFunction = table2array(readtable("triangularMembershipFunction.csv"));
figure; plot(triangularMembershipFunction,'-o')