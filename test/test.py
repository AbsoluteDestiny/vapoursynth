import unittest
import vapoursynth as vs

class CoreTestSequence(unittest.TestCase):
    
    def setUp(self):
        self.core = vs.get_core(threads=10)

    # core argument tests
    def test_num_threads(self):
        self.assertEqual(self.core.num_threads, 10)
        
    def test_func1(self):
        with self.assertRaises(vs.Error):
            self.core.blah.list_functions()
            
    def test_arg1(self):
        self.core.std.BlankClip()

    def test_arg2(self):
        self.core.std.BlankClip(width=50)
        
    def test_arg3(self):
        self.core.std.BlankClip(width=[50])
        
    def test_arg4(self):
        with self.assertRaises(vs.Error):
            self.core.std.BlankClip(width=[50, 50])
        
    def test_arg5(self):
        with self.assertRaises(vs.Error):
            self.core.std.BlankClip(width=[])
        
    def test_arg6(self):
        self.core.std.BlankClip(_width=50)
        
    def test_arg7(self):
        with self.assertRaises(vs.Error):
            self.core.std.BlankClip(_width=[])
        
    def test_arg8(self):
        with self.assertRaises(vs.Error):
            self.core.std.BlankClip(10,10,10,10,10,10,10,10,10,10,10,10,10,10)
  
    def test_arg9(self):
        with self.assertRaises(vs.Error):
            self.core.std.BlankClip(width2=50)

    def test_arg10(self):
        with self.assertRaises(vs.Error):
            self.core.std.FlipVertical()

#lut argument tests
    def test_lut_arg1(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip, lut=list(range(256)), function=lambda x: x)

    def test_lut_arg2(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip)
        
    def test_lut_arg3(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        self.core.std.Lut(clip, lut=list(range(256)))

    def test_lut_arg4(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip, lut=list(range(257)))

    def test_lut_arg5(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip, lut=list(range(255)))

    def test_lut_arg6(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip, lut=list(range(255)), function=lambda x: x)

    def test_lut_arg7(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip, lut=list(range(255)), function=lambda x: x + 1)
        
    def test_lut_arg8(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        self.core.std.Lut(clip, function=lambda x: x)

    def test_lut_arg9(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut(clip, function=lambda x: x, planes=[3])
            
#lut2 argument tests
    def test_lut2_arg1(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip], lut=[5]*65536, function=lambda x,y: (x+y)/2)

    def test_lut2_arg2(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip])
        
    def test_lut2_arg3(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        self.core.std.Lut2([clip, clip], lut=[5]*65536)

    def test_lut2_arg4(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip], lut=[5]*65537)

    def test_lut2_arg5(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip], lut=[5]*65535)

    def test_lut2_arg6(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip], lut=[5]*65535, function=lambda x,y: (x+y)/2)

    def test_lut2_arg7(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip], lut=[5]*65535, function=lambda x,y: x*y)
        
    def test_lut2_arg8(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        self.core.std.Lut2([clip, clip], function=lambda x,y: (x+y)/2)

    def test_lut2_arg9(self):
        clip = self.core.std.BlankClip(format=vs.YUV420P8, color=[69, 242, 115])
        with self.assertRaises(vs.Error):
            self.core.std.Lut2([clip, clip], function=lambda x,y: (x+y)/2, planes=[3])
        
if __name__ == '__main__':
    unittest.main()
