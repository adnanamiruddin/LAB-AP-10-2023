# sec>jam; jam=sec/3600
# sec>menit; menit=sec/60


# n = int(input("masukkan jumlah sec= "))

# jam = n / (60*60)
# n = n - (( 60 * 60 )*jam)
# menit = sec / 60
# n = n - (60*menit)
# print(f"")

# main(){
#  int sec,jam,menit,sec ;

#  printf("Masukan jumlah sec yang mau dihitung : "); scanf("%d",&sec);

# jam=sec / (60*60);
# sec= sec-((60*60)*jam);
# menit=sec / 60;
# sec= sec - (60*menit);
# printf("\n===============================================");
#  printf("\nmaka waktunya adalah :  ");
#  printf("\n Jam   : %d \n Menit : %d \n sec : %d ",jam,menit,sec);

#  getch();

# }

sec = int(input("masukkan jumlah detik= "))

jam = sec // 3600
menit = (sec % 3600) // 60
sec = (sec % 3600) % 60

print (f"{jam:02d}:{menit:02d}:{sec:02d}")