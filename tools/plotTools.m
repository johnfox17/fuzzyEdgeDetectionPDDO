clear;
% close all;

addpath('../data/simData/')
addpath('../data/output/')

gradient = table2array(readtable("gradient.csv"));
figure; imagesc(reshape(gradient,[512 512]).');
colormap gray
colorbar

figure;
histogram(gradient)