// Create a Menu Driven Console Application based for simulating a Patient Management system 

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct patient_details{
    char reg_no[10];
    char first_name[10];
    char last_name[10];
    char dob[12];
    char gender[6];
    char address[50];
    char phone_no[12]; 
}Patient[100];

void main(){ 
    int n=0;
    while(1){
        int option;
        printf("\n\nChoose the option below:\n\n 1.Enter the details of a new patient\n 2.List all patients\n 3.Exit\n");
        scanf("%d",&option);
        switch(option){
            case 1 : {
                //struct patient_details Patient[n];
                printf("\n\nHello, Welcome");
                printf("\nEnter the Reg no:");
                scanf("%s",&Patient[n].reg_no);
                printf("\nEnter first_name:");
                scanf("%s",&Patient[n].first_name);
                printf("\nEnter last_name:");
                scanf("%s",&Patient[n].last_name);
                printf("\nEnter the dob as date-month-year format:");
                scanf("%s",&Patient[n].dob);
                printf("\nEnter the gender:");
                scanf("%s",&Patient[n].gender);
                printf("\nEnter address:");
                scanf("%s",&Patient[n].address);
                printf("\nEnter phone_no : ");
                scanf("%s",&Patient[n].phone_no);
                printf("\nSuccessfully completed the entry details\n\n");
                n++;
                break;
                }
                
            case 2 :{
                int m;
                if(n==0){
                	printf("\n\nNo records of the patient found\n");
                }
                else{
                for(m=0;m<n;m++){
                    printf("\n\nPatient_%d : ",m);
                    printf("%s",Patient[m].reg_no);
                    printf("\t%s",Patient[m].first_name);
                    printf("\t%s",Patient[m].last_name);
                    printf("\t%s",Patient[m].dob);
                    printf("\t%s",Patient[m].gender);
                    printf("\t%s",Patient[m].address);
                    printf("\t%s",Patient[m].phone_no);
                }
              	}
                break;
		}	
            
            case 3:{
                printf("\n\nThanking You for contacting us. See u later\n");
                exit(0);
                
        }
        default:{
        	printf("\n\nEnter a valid option\n");
        	break;
        }
        }
    }
}
