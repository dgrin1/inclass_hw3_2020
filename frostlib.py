{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "\n",
    "def fsin(x):\n",
    "#take arg mod 2pi\n",
    "        x=x%(2.e0*np.pi)\n",
    "#initialize iterator and sum\n",
    "        i = 0\n",
    "        s,sold = 0.e0,0.e0\n",
    "\n",
    "#Keep at most 10000 terms in the Taylor series\n",
    "        for i in range(10000):\n",
    "                sold=s\n",
    "                s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))\n",
    "#If converged to machine precision then break out of loop\n",
    "                if sold==s: break\n",
    "        return s\n",
    "\n",
    "def fcos(x):\n",
    "    #initialize iterator and sum\n",
    "        i = 0\n",
    "        s,sold = 0.e0,0.e0\n",
    "\n",
    "#Keep at most 10000 terms in the Taylor series\n",
    "        for i in range(10000):\n",
    "                sold=s\n",
    "                s+= float((((-1)**i) * (x**((2*i) ))))/float(math.factorial(((2*i) )))\n",
    "#If converged to machine precision then break out of loop\n",
    "                if sold==s: break\n",
    "        return s\n",
    "    \n",
    "def ftan(x):\n",
    "    s = fsin(x)/fcos(x)\n",
    "    return s\n",
    "\n",
    "def fsec(x):\n",
    "    s = 1/fcos(x)\n",
    "    return s\n",
    "\n",
    "def fcsc(x):\n",
    "    s=1/fsin(x)\n",
    "    return s\n",
    "\n",
    "def fcot(x):\n",
    "    s=fcos(x)/fsin(x)\n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-1.0101086659079936\n"
     ]
    }
   ],
   "source": [
    "print(fsec(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
