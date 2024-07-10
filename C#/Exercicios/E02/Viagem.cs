class Viagem {
    private double d = 0;
    private double t = 0;

    public void SetDistancia(double x){
        if(x >= 0) d = x;
        else throw new ArgumentOutOfRangeException();
    }
    public void SetTempo(double x){
        if(x >= 0) t = x;
        else throw new ArgumentOutOfRangeException();
    }

    public double GetTempo(){
        return t;
    }
    public double GetDist(){
        return d;
        }
    public double Calc_velo(){
        return d/(t/60);
    }
}   
