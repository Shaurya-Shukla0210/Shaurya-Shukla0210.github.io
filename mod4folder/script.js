var names=new Array();
names[0]="harsh";
names[1]="Jason";
names[2]="rapid";
names[3]="jenny";
names[4]="shivam";
names[5]="jen";
names[6]="pqr";
names[7]="st";



for (var i = 0; i < names.length; i++) {
	if(names[i].charAt(0)==='J'|| names[i].charAt(0)==='j'){
        console.log("Goodbye "+ names[i])
	}
	else{
		console.log("Hello "+ names[i])
	}
}