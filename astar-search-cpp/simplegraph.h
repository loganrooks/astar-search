#ifndef SIMPLEGRAPH_H
#define SIMPLEGRAPH_H

template<typename T>
class SimpleGraph
{
private:
    typedef T Location;
    typedef typename vector<Location>::iterator iterator;
    unordered_map<Location, vector<Location>> edges;
public:
    SimpleGraph();

};

#endif // SIMPLEGRAPH_H
