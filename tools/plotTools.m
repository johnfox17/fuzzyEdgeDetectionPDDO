clear;
close all;

addpath('../data/simData/')
addpath('../data/output/')

fuzzyMembershipImage = table2array(readtable("fuzzyMembershipImage.csv"));
figure; imagesc(reshape(fuzzyMembershipImage,[516 516]));
colormap gray
