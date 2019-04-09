ComplexityPath = '/Users/CesarMB13/Google Drive/Conferences/2019/LANET2019/medyfinol/output';
NetIntPath = '/Users/CesarMB13/Google Drive/Conferences/2019/LANET2019/medyfinol/LANET2019/output';

% Complexity = zeros(50000,1);
% NetInt = zeros(50000,1);
% 
% % Cargar Complexities
% listing = dir(strcat(ComplexityPath,'/*.txt'));
% for n=1:length(listing)
%     v = str2num(listing(n).name(13:end-4));
%     A = importdata(strcat(ComplexityPath,'/',listing(n).name));
%     Complexity((v-1)*10+1:v*10) = A(:,3);
%     disp([num2str(n),' de 5000'])
% end
% 
% % Cargar NetInt
% listing = dir(strcat(NetIntPath,'/*.txt'));
% for n=1:length(listing)
%     v = str2num(listing(n).name(11:end-4));
%     b = importdata(strcat(NetIntPath,'/',listing(n).name));
%     NetInt((v-1)*10+1:v*10) = b;
%     disp([num2str(n),' de 5000'])
% end
% 
% save('results.mat', 'Complexity', 'NetInt')
load('results.mat')

X = [Complexity,NetInt];
hist3(X,'CDataMode','auto','FaceColor','interp')
xlabel('Complexity')
ylabel('NetInt')

ind_central = find(NetInt < 2 & NetInt >-2);
ind_sup = find(NetInt > 1);
ind_inf = find(NetInt < -1 & NetInt >-5);

ComplexSup = Complexity(ind_sup);
ComplexInf = Complexity(ind_inf);
ComplexCentral = Complexity(ind_central);

figure
h1 = histogram(ComplexInf,50,'Normalization','probability');
figure
h2 = histogram(ComplexCentral,50,'Normalization','probability');
figure
h3 = histogram(ComplexSup,50,'Normalization','probability');




