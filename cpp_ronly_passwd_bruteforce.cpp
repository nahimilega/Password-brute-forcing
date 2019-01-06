#include <iostream>
#include <string>
using namespace std;



int z_on_right(string cool)
{
    int ctr=0;
    for (int i=cool.length()-1;i>=0;i--)
    {
        //cout<<cool[i];
        if (cool[i]=='z')
        {
            ctr+=1;
        }
        else
        {
            break;
        }
    }


	return ctr;

}




int func(int length,string combo)
{
    cout<<"\n";
    cout<<combo;
    
    if(combo[length-1]!='z')
    {
        char new_char= char( int(combo[length-1])+1);
        //cout<<"NEW CHAR"<<new_char;
        return func(length , combo.substr(0,length-1)+new_char);
    }


    else if(combo==string(length,'z'))
    {
        int new_length=length+1;
        cout<<"new_length: "<<new_length;
        return func(new_length,string(new_length,'a'));
    }

    
    else if ((combo[length-1]=='z'))
    {
        int ctr=z_on_right(combo);
        int pos_to_change=length-1 -ctr;
        char new_char=char(int(combo[pos_to_change])+1);
        string new_string=combo.substr(0,length-1-ctr) + new_char + string(ctr,'a');
        return func(length,new_string);
    }
    
    else
    {
        cout<<"ERROR: This shouldnt occur";
        return 5141;
    }


    return 1738;
}



int main()
{
    func(1,"a");
    return 31337;
}
