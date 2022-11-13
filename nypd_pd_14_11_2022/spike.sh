sed -n '/spike/,/>/{ /spike/! { />/! p } }' NC_002306.faa > out1.txt
sed -n '/spike/,/>/{ /spike/! { />/! p } }' NC_010437.faa > out2.txt
