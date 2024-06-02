clear;
% close all;

addpath('../data/simData/')
addpath('../data/output/')

F = table2array(readtable("D.csv"));
figure; imagesc(reshape(abs(F),[516 516]).');
colormap gray
colorbar

figure;
histogram(F)