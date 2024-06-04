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

laplacianPDDO = table2array(readtable("laplacianPDDO.csv"));
laplacianPDDO = abs(laplacianPDDO./max(abs(laplacianPDDO(:))));
% laplacianPDDO(laplacianPDDO<.15)=0;
% laplacianPDDO(laplacianPDDO~=0)=1;
figure;
imagesc(laplacianPDDO)
colormap gray
colorbar






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