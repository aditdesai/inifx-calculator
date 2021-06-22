#include <iostream>
#include <stack>

using namespace std;

bool isOperand(char c)
{
    return c >= '0' && c <= '9';
}

int prec(char c)
{
    if(c == '*' || c == '/')
        return 2;
    else if(c == '+' || c == '-')
        return 1;
    else
        return 0;
}

double evaluate(double a, double b, int op)
{
    if(op == '+')
        return a + b;
    else if(op == '-')
        return a - b;
    else if(op == '*')
        return a * b;
    else if(op == '/')
        return a / b;
    
    return 0;
}

double evaluateInfix(string &exp)
{
    int l = exp.size();

    stack<double> operands;
    stack<char> operators;

    char c;
    for(int i = 0; i < l; ++i)
    {
        c = exp[i];

        if(c == ' ')
            continue;
    
        if(isOperand(c))
        {
            string temp = "";
            temp += c;
            while(isOperand(exp[++i]))
            {
                temp += exp[i];
            }
            i--;
            operands.push(stod(temp));
        }

        else if(c == ')')
        {
            while(!operators.empty() && operators.top() != '(')
            {
                double num1 = operands.top();
                operands.pop();
                double num2 = operands.top();
                operands.pop();

                operands.push(evaluate(num2, num1, operators.top()));
                operators.pop();
            }
            operators.pop();
        }

        else if(c == '(')
        {
            operators.push(c);
        }

        else
        {
            while(!operators.empty() && c != '(' && prec(c) <= prec(operators.top()))
            {
                double num1 = operands.top();
                operands.pop();
                double num2 = operands.top();
                operands.pop();

                operands.push(evaluate(num2, num1, operators.top()));
                operators.pop();
            }
            operators.push(c);
        }
    }

    while(!operators.empty())
    {
        double num1 = operands.top();
        operands.pop();
        double num2 = operands.top();
        operands.pop();

        operands.push(evaluate(num2, num1, operators.top()));
        operators.pop();
    }

    return operands.top();
}

int main()
{
    string exp;
    cout << "Enter expression: ";
    getline(cin, exp);

    double result = evaluateInfix(exp);
    cout << result << endl;

    return 0;
}