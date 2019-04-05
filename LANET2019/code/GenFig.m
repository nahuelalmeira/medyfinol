ComplexityPath = '/Users/CesarMB13/Google Drive/Conferences/2019/LANET2019/medyfinol/output';
NetIntPath = '/Users/CesarMB13/Google Drive/Conferences/2019/LANET2019/medyfinol/LANET2019/output';

Complexity = zeros(50000,1);
NetInt = zeros(50000,1);

% Cargar Complexities
listing = dir(strcat(ComplexityPath,'/*.txt'));
for n=1:length(listing)
    v = str2num(listing(n).name(13:end-4));
    A = importdata(strcat(ComplexityPath,'/',listing(n).name));
    Complexity((v-1)*10+1:v*10) = A(:,3);
    disp([num2str(n),' de 5000'])
end

% Cargar NetInt
listing = dir(strcat(NetIntPath,'/*.txt'));
for n=1:length(listing)
    v = str2num(listing(n).name(11:end-4));
    b = importdata(strcat(NetIntPath,'/',listing(n).name));
    NetInt((v-1)*10+1:v*10) = b;
    disp([num2str(n),' de 5000'])
end

save('results.mat', 'Complexity', 'NetInt')






