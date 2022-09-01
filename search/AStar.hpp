
#include <cstddef>

#include <list>
#include <queue>
#include <tuple>

using namespace std;

namespace GNC {
namespace ASTAR {

/*
 * @brief Node class used with the AStar search.
 * @description Nodes maybe "linked" to build a graph of nodes. Caution must be
 * taken when linking nodes. The graph is linked from the goal back
 * @param bool identifies if it should be considered a goal
 */
template <class D> class Node {
public:
  Node() {
    this->fCost = 0;
    this->gCost = 0;
    this->cameFrom = NULL;
    this->closed = false;
  }

  Node(const Node &node) {
    this->fCost = node.fCost;
    this->gCost = node.gCost;
    this->neighbors = node.neighbors;
    this->cameFrom = node.cameFrom;
    this->closed = node.closed;
  }

  ~Node() {}

  // Operator used with AStar priority queue (openSet).
  // Represents the fCost comparison between two nodes for ordering purposes
  // within the queue
  bool operator()(const Node<D> *lhs, const Node<D> *rhs) const {
    bool test = false;

    if (lhs->getFcost() > rhs->getFcost()) {
      test = true;
    }

    return test;
  }

  // Sets the current nodes G & F costs along with the "from" address of the
  // parent
  bool set(Node<D> *parent, D cost, D guess) {

    bool isSet = false;

    if (cameFrom == NULL || this->gCost > parent->getGcost() + cost) {

      this->gCost = parent->getGcost() + cost;
      this->fCost = gCost + guess;
      this->cameFrom = parent;

      isSet = true;
    }

    return isSet;
  }

  // Links the Node,Cost tuple of the nodes neighbors
  void link(Node<D> *node, D cost) {
    neighbors.push_back(tuple<Node<D> *, D>(node, cost));
  }

  // Returns the current F cost of the node
  D getFcost() const { return fCost; }

  // Returns the current G cost of the node
  D getGcost() const { return gCost; }

  // Returns a pointer to the current list of Nodes pointers and associated
  // costs to the respective neighbor
  list<tuple<Node<D> *, D>> *getNeighbors() { return &neighbors; }

  // Marks the current node as closed
  void close() { closed = true; }

  // Returns if the current node is closed
  bool isClosed() { return closed; }

  // Returns the pointer in which the currnet node is linked from
  Node<D> *from() { return cameFrom; }

private:
  D gCost;
  D fCost;

  Node<D> *cameFrom;
  list<tuple<Node<D> *, D>> neighbors;

  bool closed;
};

template <class N, N (*heuristic)(Node<N> from, Node<N> goal)> class AStar {

public:
  AStar() { this->solution = false; }

  bool search(Node<N> *start, Node<N> *goal) {

    openSet.push(start);
    // int i = 0;

    while (!openSet.empty()) {

      current = openSet.top();
      openSet.pop();

      current->close();

      if (current == goal) {
        solution = true;
        break;
      }

      for (tuple<Node<N> *, N> neighbor : *current->getNeighbors()) {

        Node<N> *node = std::get<Node<N> *>(neighbor);
        N cost = std::get<N>(neighbor);

        if (node->isClosed()) {
          continue;
        }

        if (node->set(current, cost, heuristic(*node, *goal))) {
          openSet.push(node);
        }
      }
    }

    return solution;
  }

private:
  priority_queue<Node<N>, vector<Node<N> *>, Node<N>> openSet;
  Node<N> *current;

  bool solution;
};

} // namespace ASTAR
} // namespace GNC
