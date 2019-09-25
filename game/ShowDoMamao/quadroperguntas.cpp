include "quadroperguntas.h"
#include "ui_quadroperguntas.h"

quadroPerguntas::quadroPerguntas(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::quadroPerguntas)
{
    ui->setupUi(this);
}

quadroPerguntas::~quadroPerguntas()
{
    delete ui;
}
