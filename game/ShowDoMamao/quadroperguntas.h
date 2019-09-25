#ifndef QUADROPERGUNTAS_H
#define QUADROPERGUNTAS_H

#include <QDialog>

namespace Ui {
class quadroPerguntas;
}

class quadroPerguntas : public QDialog
{
    Q_OBJECT

public:
    explicit quadroPerguntas(QWidget *parent = nullptr);
    ~quadroPerguntas();

private:
    Ui::quadroPerguntas *ui;
};

#endif // QUADROPERGUNTAS_H
