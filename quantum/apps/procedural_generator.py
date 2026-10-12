#!/usr/bin/env python3
"""Model QK deterministic procedural quantum circuit generator."""
from __future__ import annotations
import argparse, hashlib, math, random
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Config:
    seed:int
    qubits:int
    depth:int
    algorithm:str
    theta:float=math.pi/4

class Generator:
    def __init__(self,c:Config):
        if not 1<=c.qubits<=24: raise ValueError("qubits must be 1..24")
        if not 1<=c.depth<=10000: raise ValueError("depth must be 1..10000")
        self.c=c; self.r=random.Random(c.seed)

    def pair(self):
        a=self.r.randrange(self.c.qubits); b=self.r.randrange(self.c.qubits-1)
        if b>=a: b+=1
        return a,b

    def random_layer(self,i):
        out=[]; gates=["x","y","z","h","s","t"]
        for q in range(self.c.qubits):
            if self.r.random()<.45: out.append(f"{self.r.choice(gates)} q[{q}];")
        for _ in range(self.c.qubits//2):
            if self.r.random()<.65:
                a,b=self.pair(); out.append(f"cx q[{a}], q[{b}];")
        if i%4==0: out.append(f"rz({self.c.theta:.12g}) q[{i%self.c.qubits}];")
        return out

    def qft(self):
        out=[]
        for j in range(self.c.qubits):
            out.append(f"h q[{j}];")
            for k in range(j+1,self.c.qubits):
                out.append(f"cp({math.pi/(2**(k-j)):.12g}) q[{k}], q[{j}];")
        for j in range(self.c.qubits//2):
            out.append(f"swap q[{j}], q[{self.c.qubits-1-j}];")
        return out

    def grover(self):
        if self.c.qubits<2: raise ValueError("grover requires at least 2 qubits")
        target=self.r.randrange(1<<self.c.qubits)
        out=[f"h q[{q}];" for q in range(self.c.qubits)]
        for q in range(self.c.qubits):
            if not(target>>q)&1: out.append(f"x q[{q}];")
        out.append(f"// procedural oracle target={target}")
        for q in range(self.c.qubits-1): out.append(f"cx q[{q}], q[{self.c.qubits-1}];")
        out.append(f"h q[{self.c.qubits-1}];")
        return out

    def variational(self):
        out=[]
        for l in range(self.c.depth):
            for q in range(self.c.qubits):
                a=self.c.theta*math.sin((l+1)*(q+1))
                out.append(f"ry({a:.12g}) q[{q}];")
            for q in range(self.c.qubits-1): out.append(f"cx q[{q}], q[{q+1}];")
        return out

    def generate(self):
        if self.c.algorithm=="random": ops=[x for i in range(self.c.depth) for x in self.random_layer(i)]
        elif self.c.algorithm=="qft": ops=self.qft()
        elif self.c.algorithm=="grover": ops=self.grover()
        elif self.c.algorithm=="variational": ops=self.variational()
        else: raise ValueError("unknown algorithm")
        digest=hashlib.sha256("\n".join(ops).encode()).hexdigest()
        return "\n".join(["OPENQASM 3.0;",'include "stdgates.inc";',
            f"// Model QK procedural circuit seed={self.c.seed} algorithm={self.c.algorithm}",
            f"// sha256={digest}",f"bit[{self.c.qubits}] c;",f"qubit[{self.c.qubits}] q;",
            *ops,"measure q -> c;",""]) 

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--seed",type=int,default=20261011)
    p.add_argument("--qubits",type=int,default=4)
    p.add_argument("--depth",type=int,default=8)
    p.add_argument("--algorithm",choices=["random","qft","grover","variational"],default="random")
    p.add_argument("--theta",type=float,default=math.pi/4)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    s=Generator(Config(a.seed,a.qubits,a.depth,a.algorithm,a.theta)).generate()
    if a.output: a.output.write_text(s,encoding="utf-8")
    else: print(s,end="")
if __name__=="__main__": main()
